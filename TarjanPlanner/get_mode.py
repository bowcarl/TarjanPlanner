from vehicle import Vehicle

def get_mode_of_transport(transport_data, mode_of_transport, transport_list):
    # Validate mode of transport
    valid_modes = [mode["Mode"].lower() for mode in transport_data["Modes_of_Transport"]]
    while mode_of_transport not in valid_modes:
        print("Invalid mode of transport. Please try again.")
        mode_of_transport = input("Enter the mode of transport: ").strip().lower()

    transport_list.append(mode_of_transport)

    # Create a Vehicle instance for the selected mode of transport
    for mode in transport_data["Modes_of_Transport"]:
        if mode["Mode"].lower() == mode_of_transport:
            return Vehicle(
                mode=mode["Mode"],
                speed_kmh=mode["Speed_kmh"],
                cost_per_km=mode["Cost_per_km"],
                transfer_time_min=mode["Transfer_Time_min"]
            ), transport_list