from tabulate import tabulate #import tabulate agar tabel yang ditambilkan jadi lebih bagus 

DictStudent = {
    "X" : {
        "Name" : ["Andi", "Budi", "Cinta"],
        "NIS" : [20260101, 20260203, 20260305],
        "Gender": ["M", "M", "F"],
        "Subject":
            ["Math", "English", "Bahasa", "Science"],
        "Nilai": [
            [60, 70, 85, 60], 
            [90, 60, 50, 85],
            [80, 75, 85, 70]
        ] 
        },
    "XI" : {
        "Name" : ["Dita", "Erwin", "Fani"],
        "NIS" : [20250109, 20250208, 20250311],
        "Gender": ["F", "M", "F"],
        "Subject": 
            ["Math", "English", "Bahasa", "Science"],
        "Nilai": [
            [70, 70, 85, 75], 
            [90, 90, 95, 85],
            [60, 40, 95, 65]
        ] 
    },
    "XII" : {
        "Name" : ["Genta", "Hana", "Ijat"],
        "NIS" : [20240110, 20240213, 20240311],
        "Gender": ["M", "F", "M"],
        "Subject": 
            ["Math", "English", "Bahasa", "Science"],
        "Nilai": [
            [60, 50, 65, 60], 
            [95, 90, 80, 85],
            [100, 65, 75, 95]
        ] 
    }
}

def choose_class():
# Memilih kelas
    while True:
        choosecls = input("\nInput your class (X/XI/XII): ").upper()
        print()
        if choosecls in ["X", "10"]:
            return  "X"
        elif choosecls in ["XI", "11"]:
            return "XI"
        elif choosecls in ["XII", "12"]:
            return "XII"
        else:
            print("Unknown Class!")

def show_table(chooscls):
 # Ambil Data Berdasarkan Kelas
        data = DictStudent[choosecls]

        tablemenu1 = []

        print(f"{f' {choosecls} CLASS DATA ':=^74}")

# Menampilkan data siswa 

        for i in range(len(data["Name"])):
            tablemenu1.append([
                i+1,
                data["NIS"][i],
                data["Name"][i],
                data["Gender"][i],
                data["Nilai"][i][0],
                data["Nilai"][i][1],
                data["Nilai"][i][2],
                data["Nilai"][i][3]
                  ])
            
        print(tabulate(tablemenu1, 
                       headers=["No","NIS","Name","Gender","Math", "English", "Bahasa", "Science"]))

def add_student(choosecls):

    data = DictStudent[choosecls]

    input_name = input("\nInput student Name: ").capitalize()

    input_NIS = int(input("Input student NIS: "))

    # Validasi NIS
    if input_NIS in data["NIS"]:
        print("NIS already Exists!")
        return

    # Validasi Gender
    while True:
        input_Gender = input("Input student Gender (M/F): ").lower()
    
        if input_Gender in ["m", "male", "laki", "lelaki", "laki-laki", "laki laki"]:
            input_Gender = "M"
            break

        if input_Gender in ["f", "female", "perempuan", "wanita" ]:
            input_Gender = "F"
            break

        else:
            print("Invalid gender!")

    # Input Nilai
    input_math = int(input("Input student Math score: "))
    input_english = int(input("Input student English score: "))
    input_bahasa = int(input("Input student Bahasa score: "))
    input_science = int(input("Input student Science score: "))


    # Menambahkan Data
    DictStudent[choosecls]["Name"].append(input_name)
    DictStudent[choosecls]["NIS"].append(input_NIS)
    DictStudent[choosecls]["Gender"].append(input_Gender)

    # Menambahkan nilai
    DictStudent[choosecls]["Nilai"].append(
                        [input_math, input_english, input_bahasa, input_science]
                    )
    
    print("\nSTUDENT SUCCESFULLY ADDED!")
    print()
    show_table(choosecls)


def update_student(choosecls):

    data = DictStudent[choosecls]

    show_table(choosecls)

    inp_NIS = int(input("\nInput student NIS: ")) # input NIS 

    if inp_NIS in data["NIS"]:   
        student_index = data["NIS"].index(inp_NIS) # dicek apakah NIS ada pada data
    
        print("""
            Choose subject:
            1. Math 
            2. English
            3. Bahasa
            4. Science
            """)
    
        choose_subject = int(input("Input subject (1/2/3/4): ")) # memilih subject yang ingin di update
    
        if choose_subject in [1,2,3,4]:
            subject_index = choose_subject - 1  # Math -> 0, English -> 1
            new_score = int(input("Input student new score: ")) # input nilai yang ingin di masukkan 

        # Validasi Nilai 
            if 0 <= new_score <= 100:
                data["Nilai"][student_index][subject_index] = new_score 
                print("\nSTUDENT SCORE SUCCESFULLY UPDATED!")
        # Menampilkan tabel setelah terupdate
                show_table(choosecls)

            else:
                print("Score must be between 0 and 100!")
    
        else:
            print("Unknown subject!")
    
    else:
        print("NIS not found!")


def delete_student(choosecls):

    data = DictStudent[choosecls]

    show_table(choosecls)

    i_nis = int(input("\nInput Student NIS to delete: "))
    if i_nis in data["NIS"]:
        index_student = data["NIS"].index(i_nis)

        # konfirmasi delete
        confirmdel = input(
            "Are you sure you want to delete this student? (Yes/No): "
        ).strip().lower()

        if confirmdel in ["yes", "ya", "y"]:
            for key in ["Name", "NIS", "Gender", "Nilai"]:
                data[key].pop(index_student)
    
            print("\nSTUDENT SUCCESFULLY DELETED!!!")
    
            # Menampilkan data setelah dihapus
            show_table(choosecls)

        elif confirmdel in ["no", "tidak", "n"]:
            print("\nDelete cancelled")

        else:
            print("\nInvalid input")

    else:
        ("NIS not Found!")

    
# MENU CODE
while True: 

    print(f"""
    {"=".center(60, "=")}
    {"Welcome to Student Academic Data".center(60)}
    {"XYZ High School".center(60)} 
    {"=".center(60, "=")}

    MAIN MENU
    1. Read Student Data
    2. Add Student Data
    3. Update Student Score
    4. Delete Student Data
    5. Exit
    """)

    menu = int(input("Input your menu: "))

    if menu == 1:
        choosecls = choose_class()

        show_table(choosecls)

    elif menu == 2:
        choosecls = choose_class()

        add_student(choosecls)

    elif menu == 3:
        choosecls = choose_class() 

        update_student(choosecls)
    
    elif menu == 4:
        choosecls = choose_class()

        delete_student(choosecls)

    elif menu == 5:
        print("THANK YOU")
        break

    else:
        print("Unknown Menu!!")
