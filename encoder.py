def main():
    encode_dict = {"A": "00", "C": "11", "G": "01", "T": "10"}
    seq = input("Seq: ").upper()
    encode_seq = [encode_dict[nuc] for nuc in seq]
    print("".join(encode_seq))

main()
