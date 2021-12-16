from abc import ABC, abstractmethod
from collections import namedtuple

Header = namedtuple("Header", "version type_id")


def read_input():
    with open("inputs/day_16.txt") as file:
        return file.readline().strip()


class Packet(ABC):
    def __init__(self, header):
        self.header = header
        self.sub_packets = []

    def add_packet(self, packet):
        self.sub_packets.append(packet)

    def get_version(self):
        return self.header.version

    @abstractmethod
    def get_value(self):
        pass


class LiteralPacket(Packet):
    def __init__(self, header, binary):
        super().__init__(header)
        self.value = to_number(binary)

    def get_value(self):
        return self.value


class SumPacket(Packet):
    def get_value(self):
        return sum(c.get_value() for c in self.sub_packets)


class ProductPacket(Packet):
    def get_value(self):
        val = 1
        for p in self.sub_packets:
            val *= p.get_value()
        return val


class MinimumPacket(Packet):
    def get_value(self):
        return min(p.get_value() for p in self.sub_packets)


class MaximumPacket(Packet):
    def get_value(self):
        return max(p.get_value() for p in self.sub_packets)


class GreaterThanPacket(Packet):
    def get_value(self):
        return 1 if self.sub_packets[0].get_value() > self.sub_packets[1].get_value() else 0


class LessThanPacket(Packet):
    def get_value(self):
        return 1 if self.sub_packets[0].get_value() < self.sub_packets[1].get_value() else 0


class EqualToPacket(Packet):
    def get_value(self):
        return 1 if self.sub_packets[0].get_value() == self.sub_packets[1].get_value() else 0


def operator_factory(header):
    if header.type_id == 0:
        return SumPacket(header)
    elif header.type_id == 1:
        return ProductPacket(header)
    elif header.type_id == 2:
        return MinimumPacket(header)
    elif header.type_id == 3:
        return MaximumPacket(header)
    elif header.type_id == 5:
        return GreaterThanPacket(header)
    elif header.type_id == 6:
        return LessThanPacket(header)
    elif header.type_id == 7:
        return EqualToPacket(header)
    else:
        raise ValueError(f"Unrecognised type_id {header.type_id}")


class BitsDecoder:
    def __init__(self, hex_transmission):
        self.binary = to_binary(hex_transmission)
        # program counter, contains index of current bit in binary
        self.pc = 0

    def decode(self):
        header = self.parse_header()
        return self.parse_literal(header) if header.type_id == 4 else self.parse_operator(header)

    def parse_header(self):
        version = self.advance(3)
        type_id = self.advance(3)
        return Header(to_number(version), to_number(type_id))

    def parse_literal(self, header):
        val = ""
        while True:
            bits = self.advance(5)
            val += bits[1:]

            if bits[0] == "0":
                break

        return LiteralPacket(header, val)

    def parse_operator(self, header):
        operator = operator_factory(header)
        len_type_id = self.advance(1)

        if len_type_id == "0":
            return self.parse_operator_0(operator)
        elif len_type_id == "1":
            return self.parse_operator_1(operator)
        else:
            raise ValueError(f"Unrecognised operator length type ID {len_type_id}")

    def parse_operator_0(self, operator):
        total_bits = to_number(self.advance(15))
        start = self.pc

        while self.pc - start < total_bits:
            packet = self.decode()
            operator.add_packet(packet)

        return operator

    def parse_operator_1(self, operator):
        total_sub_packets = to_number(self.advance(11))

        while len(operator.sub_packets) != total_sub_packets:
            packet = self.decode()
            operator.add_packet(packet)

        return operator

    def advance(self, n):
        """
        Returns next n bits and increases program counter by n
        :param n: number of bits to move program counter
        :return: the bits covered
        """
        bits = self.binary[self.pc:self.pc + n]
        self.pc += n
        return bits


def to_number(binary):
    return int(binary, 2)


def to_binary(hex_transmission):
    return bin(int(hex_transmission, 16))[2:]


def get_outermost_packet():
    transmission = read_input()
    decoder = BitsDecoder(transmission)
    return decoder.decode()


def part_one():
    outer_packet = get_outermost_packet()
    packets = [outer_packet]
    version_sum = 0
    while packets:
        packet = packets.pop()
        version_sum += packet.get_version()
        packets += packet.sub_packets
    return version_sum


def part_two():
    return get_outermost_packet().get_value()


assert part_one() == 920
assert part_two() == 10185143721112
