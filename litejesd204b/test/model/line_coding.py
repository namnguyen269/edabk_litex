#
# This file is part of LiteJESD204B
#
# Copyright (c) 2016-2019 Florent Kermarrec <florent@enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause

from litex.soc.cores.code_8b10b import disparity

from test.model.common import Control

# line coding
line_coding_data_rd_m = [
    0b1001110100, 0b0111010100, 0b1011010100, 0b1100011011,
    0b1101010100, 0b1010011011, 0b0110011011, 0b1110001011,
    0b1110010100, 0b1001011011, 0b0101011011, 0b1101001011,
    0b0011011011, 0b1011001011, 0b0111001011, 0b0101110100,
    0b0110110100, 0b1000111011, 0b0100111011, 0b1100101011,
    0b0010111011, 0b1010101011, 0b0110101011, 0b1110100100,
    0b1100110100, 0b1001101011, 0b0101101011, 0b1101100100,
    0b0011101011, 0b1011100100, 0b0111100100, 0b1010110100,
    0b1001111001, 0b0111011001, 0b1011011001, 0b1100011001,
    0b1101011001, 0b1010011001, 0b0110011001, 0b1110001001,
    0b1110011001, 0b1001011001, 0b0101011001, 0b1101001001,
    0b0011011001, 0b1011001001, 0b0111001001, 0b0101111001,
    0b0110111001, 0b1000111001, 0b0100111001, 0b1100101001,
    0b0010111001, 0b1010101001, 0b0110101001, 0b1110101001,
    0b1100111001, 0b1001101001, 0b0101101001, 0b1101101001,
    0b0011101001, 0b1011101001, 0b0111101001, 0b1010111001,
    0b1001110101, 0b0111010101, 0b1011010101, 0b1100010101,
    0b1101010101, 0b1010010101, 0b0110010101, 0b1110000101,
    0b1110010101, 0b1001010101, 0b0101010101, 0b1101000101,
    0b0011010101, 0b1011000101, 0b0111000101, 0b0101110101,
    0b0110110101, 0b1000110101, 0b0100110101, 0b1100100101,
    0b0010110101, 0b1010100101, 0b0110100101, 0b1110100101,
    0b1100110101, 0b1001100101, 0b0101100101, 0b1101100101,
    0b0011100101, 0b1011100101, 0b0111100101, 0b1010110101,
    0b1001110011, 0b0111010011, 0b1011010011, 0b1100011100,
    0b1101010011, 0b1010011100, 0b0110011100, 0b1110001100,
    0b1110010011, 0b1001011100, 0b0101011100, 0b1101001100,
    0b0011011100, 0b1011001100, 0b0111001100, 0b0101110011,
    0b0110110011, 0b1000111100, 0b0100111100, 0b1100101100,
    0b0010111100, 0b1010101100, 0b0110101100, 0b1110100011,
    0b1100110011, 0b1001101100, 0b0101101100, 0b1101100011,
    0b0011101100, 0b1011100011, 0b0111100011, 0b1010110011,
    0b1001110010, 0b0111010010, 0b1011010010, 0b1100011101,
    0b1101010010, 0b1010011101, 0b0110011101, 0b1110001101,
    0b1110010010, 0b1001011101, 0b0101011101, 0b1101001101,
    0b0011011101, 0b1011001101, 0b0111001101, 0b0101110010,
    0b0110110010, 0b1000111101, 0b0100111101, 0b1100101101,
    0b0010111101, 0b1010101101, 0b0110101101, 0b1110100010,
    0b1100110010, 0b1001101101, 0b0101101101, 0b1101100010,
    0b0011101101, 0b1011100010, 0b0111100010, 0b1010110010,
    0b1001111010, 0b0111011010, 0b1011011010, 0b1100011010,
    0b1101011010, 0b1010011010, 0b0110011010, 0b1110001010,
    0b1110011010, 0b1001011010, 0b0101011010, 0b1101001010,
    0b0011011010, 0b1011001010, 0b0111001010, 0b0101111010,
    0b0110111010, 0b1000111010, 0b0100111010, 0b1100101010,
    0b0010111010, 0b1010101010, 0b0110101010, 0b1110101010,
    0b1100111010, 0b1001101010, 0b0101101010, 0b1101101010,
    0b0011101010, 0b1011101010, 0b0111101010, 0b1010111010,
    0b1001110110, 0b0111010110, 0b1011010110, 0b1100010110,
    0b1101010110, 0b1010010110, 0b0110010110, 0b1110000110,
    0b1110010110, 0b1001010110, 0b0101010110, 0b1101000110,
    0b0011010110, 0b1011000110, 0b0111000110, 0b0101110110,
    0b0110110110, 0b1000110110, 0b0100110110, 0b1100100110,
    0b0010110110, 0b1010100110, 0b0110100110, 0b1110100110,
    0b1100110110, 0b1001100110, 0b0101100110, 0b1101100110,
    0b0011100110, 0b1011100110, 0b0111100110, 0b1010110110,
    0b1001110001, 0b0111010001, 0b1011010001, 0b1100011110,
    0b1101010001, 0b1010011110, 0b0110011110, 0b1110001110,
    0b1110010001, 0b1001011110, 0b0101011110, 0b1101001110,
    0b0011011110, 0b1011001110, 0b0111001110, 0b0101110001,
    0b0110110001, 0b1000110111, 0b0100110111, 0b1100101110,
    0b0010110111, 0b1010101110, 0b0110101110, 0b1110100001,
    0b1100110001, 0b1001101110, 0b0101101110, 0b1101100001,
    0b0011101110, 0b1011100001, 0b0111100001, 0b1010110001
]


line_coding_data_rd_p = [
    0b0110001011, 0b1000101011, 0b0100101011, 0b1100010100,
    0b0010101011, 0b1010010100, 0b0110010100, 0b0001110100,
    0b0001101011, 0b1001010100, 0b0101010100, 0b1101000100,
    0b0011010100, 0b1011000100, 0b0111000100, 0b1010001011,
    0b1001001011, 0b1000110100, 0b0100110100, 0b1100100100,
    0b0010110100, 0b1010100100, 0b0110100100, 0b0001011011,
    0b0011001011, 0b1001100100, 0b0101100100, 0b0010011011,
    0b0011100100, 0b0100011011, 0b1000011011, 0b0101001011,
    0b0110001001, 0b1000101001, 0b0100101001, 0b1100011001,
    0b0010101001, 0b1010011001, 0b0110011001, 0b0001111001,
    0b0001101001, 0b1001011001, 0b0101011001, 0b1101001001,
    0b0011011001, 0b1011001001, 0b0111001001, 0b1010001001,
    0b1001001001, 0b1000111001, 0b0100111001, 0b1100101001,
    0b0010111001, 0b1010101001, 0b0110101001, 0b0001011001,
    0b0011001001, 0b1001101001, 0b0101101001, 0b0010011001,
    0b0011101001, 0b0100011001, 0b1000011001, 0b0101001001,
    0b0110000101, 0b1000100101, 0b0100100101, 0b1100010101,
    0b0010100101, 0b1010010101, 0b0110010101, 0b0001110101,
    0b0001100101, 0b1001010101, 0b0101010101, 0b1101000101,
    0b0011010101, 0b1011000101, 0b0111000101, 0b1010000101,
    0b1001000101, 0b1000110101, 0b0100110101, 0b1100100101,
    0b0010110101, 0b1010100101, 0b0110100101, 0b0001010101,
    0b0011000101, 0b1001100101, 0b0101100101, 0b0010010101,
    0b0011100101, 0b0100010101, 0b1000010101, 0b0101000101,
    0b0110001100, 0b1000101100, 0b0100101100, 0b1100010011,
    0b0010101100, 0b1010010011, 0b0110010011, 0b0001110011,
    0b0001101100, 0b1001010011, 0b0101010011, 0b1101000011,
    0b0011010011, 0b1011000011, 0b0111000011, 0b1010001100,
    0b1001001100, 0b1000110011, 0b0100110011, 0b1100100011,
    0b0010110011, 0b1010100011, 0b0110100011, 0b0001011100,
    0b0011001100, 0b1001100011, 0b0101100011, 0b0010011100,
    0b0011100011, 0b0100011100, 0b1000011100, 0b0101001100,
    0b0110001101, 0b1000101101, 0b0100101101, 0b1100010010,
    0b0010101101, 0b1010010010, 0b0110010010, 0b0001110010,
    0b0001101101, 0b1001010010, 0b0101010010, 0b1101000010,
    0b0011010010, 0b1011000010, 0b0111000010, 0b1010001101,
    0b1001001101, 0b1000110010, 0b0100110010, 0b1100100010,
    0b0010110010, 0b1010100010, 0b0110100010, 0b0001011101,
    0b0011001101, 0b1001100010, 0b0101100010, 0b0010011101,
    0b0011100010, 0b0100011101, 0b1000011101, 0b0101001101,
    0b0110001010, 0b1000101010, 0b0100101010, 0b1100011010,
    0b0010101010, 0b1010011010, 0b0110011010, 0b0001111010,
    0b0001101010, 0b1001011010, 0b0101011010, 0b1101001010,
    0b0011011010, 0b1011001010, 0b0111001010, 0b1010001010,
    0b1001001010, 0b1000111010, 0b0100111010, 0b1100101010,
    0b0010111010, 0b1010101010, 0b0110101010, 0b0001011010,
    0b0011001010, 0b1001101010, 0b0101101010, 0b0010011010,
    0b0011101010, 0b0100011010, 0b1000011010, 0b0101001010,
    0b0110000110, 0b1000100110, 0b0100100110, 0b1100010110,
    0b0010100110, 0b1010010110, 0b0110010110, 0b0001110110,
    0b0001100110, 0b1001010110, 0b0101010110, 0b1101000110,
    0b0011010110, 0b1011000110, 0b0111000110, 0b1010000110,
    0b1001000110, 0b1000110110, 0b0100110110, 0b1100100110,
    0b0010110110, 0b1010100110, 0b0110100110, 0b0001010110,
    0b0011000110, 0b1001100110, 0b0101100110, 0b0010010110,
    0b0011100110, 0b0100010110, 0b1000010110, 0b0101000110,
    0b0110001110, 0b1000101110, 0b0100101110, 0b1100010001,
    0b0010101110, 0b1010010001, 0b0110010001, 0b0001110001,
    0b0001101110, 0b1001010001, 0b0101010001, 0b1101001000,
    0b0011010001, 0b1011001000, 0b0111001000, 0b1010001110,
    0b1001001110, 0b1000110001, 0b0100110001, 0b1100100001,
    0b0010110001, 0b1010100001, 0b0110100001, 0b0001011110,
    0b0011001110, 0b1001100001, 0b0101100001, 0b0010011110,
    0b0011100001, 0b0100011110, 0b1000011110, 0b0101001110
]


def inverse_data_rd(table):
    inverse_table = {}
    for i in range(256):
        inverse_table[table[i]] = i
    return inverse_table


line_coding_data_rd_m_inverse = inverse_data_rd(line_coding_data_rd_m)
line_coding_data_rd_p_inverse = inverse_data_rd(line_coding_data_rd_p)


line_coding_control_rd_m = {
    0b00011100: 0b0011110100, #K28.0
    0b00111100: 0b0011111001, #K28.1
    0b01011100: 0b0011110101, #K28.2
    0b01111100: 0b0011110011, #K28.3
    0b10011100: 0b0011110010, #K28.4
    0b10111100: 0b0011111010, #K28.5
    0b11011100: 0b0011110110, #K28.6
    0b11111100: 0b0011111000, #K28.7
    0b11110111: 0b1110101000, #K23.7
    0b11111011: 0b1101101000, #K27.7
    0b11111101: 0b1011101000, #K29.7
    0b11111110: 0b0111101000  #K30.7
}


line_coding_control_rd_p = {
    0b00011100: 0b1100001011, #K28.0
    0b00111100: 0b1100000110, #K28.1
    0b01011100: 0b1100001010, #K28.2
    0b01111100: 0b1100001100, #K28.3
    0b10011100: 0b1100001101, #K28.4
    0b10111100: 0b1100000101, #K28.5
    0b11011100: 0b1100001001, #K28.6
    0b11111100: 0b1100000111, #K28.7
    0b11110111: 0b0001010111, #K23.7
    0b11111011: 0b0010010111, #K27.7
    0b11111101: 0b0100010111, #K29.7
    0b11111110: 0b1000010111  #K30.7
}


def inverse_control_rd(table):
    inverse_table = {}
    for k, v in table.items():
        inverse_table[v] = k
    return inverse_table


line_coding_control_rd_m_inverse = inverse_control_rd(line_coding_control_rd_m)
line_coding_control_rd_p_inverse = inverse_control_rd(line_coding_control_rd_p)


def encode_lanes(lanes):
    encoded_lanes = []
    for lane in lanes:
        table = "m"
        change_table = False

        encoded_lane = []
        for frame in lane:
            new_frame = []
            for octet in frame:
                if change_table:
                    table = "p" if table == "m" else "m"
                if isinstance(octet, Control):
                    if table == "p":
                        encoded_octet = line_coding_control_rd_p[octet.value]
                    else:
                        encoded_octet = line_coding_control_rd_m[octet.value]
                else:
                    if table == "p":
                        encoded_octet = line_coding_data_rd_p[octet]
                    else:
                        encoded_octet = line_coding_data_rd_m[octet]
                change_table = (disparity(encoded_octet, 10) != 0)
                new_frame.append(encoded_octet)

            encoded_lane.append(new_frame)

        encoded_lanes.append(encoded_lane)

    return encoded_lanes


def decode_lanes(lanes):
    decoded_lanes = []
    for lane in lanes:
        decoded_lane = []
        for frame in lane:
            new_frame = []
            for encoded_octet in frame:
                try:
                    octet = line_coding_data_rd_m_inverse[encoded_octet]
                except:
                    try:
                        octet = line_coding_data_rd_p_inverse[encoded_octet]
                    except:
                        try:
                            octet = Control(line_coding_control_rd_p_inverse[encoded_octet])
                        except:
                            octet = Control(line_coding_control_rd_m_inverse[encoded_octet])

                new_frame.append(octet)

            decoded_lane.append(new_frame)

        decoded_lanes.append(decoded_lane)

    return decoded_lanes
