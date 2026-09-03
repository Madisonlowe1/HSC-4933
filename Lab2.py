import statistics

heart_rate_samples={
    "J.Alvarez":[72,75,78],
    "M.Chen":[80,83],
    "R.Okafor":[65,68,70,66],
    "S.Patel":[90,95,92,88,91],
    "T.Nguyen":[77,79],
    "L.Kowalski":[68,70,69],
    "D.Osei":[98,101,95,99],
    "A.Whitfield":[74,76,75,73],
}

# patients based off of patient numbers
patients={
    str(i + 1):patient
    for i,patient in enumerate(heart_rate_samples)
}

#patient stats
def calculate_patient_stats(*args):
    """ Calculate patient statistics (*args)."""
# If there were no heart rate numbers passed, then return none
    if not args:
        return None
    return {
        "count":len(args),
        "min":min(args),
        "max":max(args),
        "mean":sum(args)/len(args),
        "median":statistics.median(args),
    }


# displaying the patient stats
def display_patient_stats(patient_name):
    """ Display patient statistics (*args)."""
    readings= heart_rate_samples.get(patient_name, [])

    stats = calculate_patient_stats(*readings)

    if stats:
        print(
            f"""
     ---Report: {patient_name}---
     Total readings: {stats['count']}
     Min: {stats['min']} BPM
     Max: {stats['max']} BPM
     Mean: {stats['mean']} BPM
     Median: {stats['median']} BPM"""
        )
    else:
        print(f"No records found for {patient_name}.")

def main():
        """ Main loop."""
        while True:
            print("Patient Menu")
            for number, patient in patients.items():
                print(f" [{number}] {patient}")
            choice = input("Enter choice (1-8/all/s): ")
            if choice == "1":
                display_patient_stats(patients["1"])
            elif choice == "2":
                display_patient_stats(patients["2"])
            elif choice == "3":
                display_patient_stats(patients["3"])
            elif choice == "4":
                display_patient_stats(patients["4"])
            elif choice == "5":
                display_patient_stats(patients["5"])
            elif choice == "6":
                display_patient_stats(patients["6"])
            elif choice == "7":
                display_patient_stats(patients["7"])
            elif choice == "8":
                display_patient_stats(patients["8"])
            elif choice == "all":
                for name in heart_rate_samples:
                    display_patient_stats(name)
            elif choice == "stop":
                print("stop program")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()