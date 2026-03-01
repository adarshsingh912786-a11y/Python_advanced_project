from database import (
    get_client_status_counts,
    get_total_clients_count,
    get_most_active_client
)

def get_status_summary():

    status_summary = {
        "lead" : 0,
        "contacted" : 0,
        "converted" : 0,
        "lost" : 0
    }

    summary = get_client_status_counts()

    if summary is None:
        return status_summary
    
    status_summary["lead"] = summary[0][1]
    status_summary["contacted"] = summary[1][1]
    status_summary["converted"] = summary[2][1]
    status_summary["lost"] = summary[3][1]

    return status_summary

def get_coversion_rate():

    total = get_total_clients_count()
    summary = get_status_summary()

    if total == 0:
        return 0.0
    
    converted = summary[2][1]

    return (converted/total)*100

def get_active_client():

    active_client = get_most_active_client()

    if active_client :
        return {
            "client_id" : active_client[0],
            "client_name" : active_client[1],
            "Interaction_count" : active_client[2]
        }
    
    return None