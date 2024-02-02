import pythonfuzz

def my_fuzzer(data):
    # Application level checks
    try:
        import my_library
        decoded_data = my_library.decode(data)
        if decoded_data != my_library.encode(decoded_data):
            raise Exception("Decode/Encode mismatch")
    except Exception as e:
        raise e

pythonfuzz.run(my_fuzzer, max_total_time=3600)