services={
    "4K Video Editing" : "$50", 
    "1080p Video Editing": "$25",
    "Photo Improvement Services":"$10"
}
# services is a dictionary (associative array), which contains a list of services provided by a company and the cost of the service.
print(services.get("4K Video Editing"))
