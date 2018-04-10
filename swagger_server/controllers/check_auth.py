def check_auth(connexion):
    auth_header_value = "Authorization"
    try:
        header_token = connexion.headers['Authorization']
    except KeyError as e:
        try:
            header_token = connexion.headers['Authorisation']
            auth_header_value = "Authorisation"
        except KeyError as k:
            return "Error Unauthorised Usage", False
    return auth_header_value,True


    # authHeaderValue = "Authorization"
    # try:
    #     header_token = connexion.request.headers['Authorization']
    # except KeyError as e:
    #     try:
    #         header_token = connexion.request.headers['Authorisation']
    #         authHeaderValue = "Authorisation"
    #     except KeyError as k:
    #         return "Error Unauthorised Usage", 401
