let a = {
    "CheckInFolio": {
        "HotelCode": "string",
        "FolioCode": "string",
        "CheckInTime": "long",
        "CheckOutTime": "long",
        "RoomNo": "array",
        "Remark": "string",
        "PMSOperateTime": "long"
    },
    "GuestSet": [{
        "Guest": {
            "HotelDocType": "number",
            "HotelDocNo": "string",
            "HotelDocName": "string",
            "HotelBornDate": "string",
            "HotelSex": "number",
            "NationaCode": "string",
            "HotelNation": "number",
            "HotelAddress": "string",
            "HotelRemark": "string",
            "HotelTel": "string",
            "IsForeigner": "number",
            "GuestDocID": "number",
            "PassNo": "string",
            "VisaDeadline": "long",
            "DepartureTime": "long",
            "EntryTime": "long",
            "EntryPlace": "string",
            "DeparturePlace": "string",
            "VisaType": "number",
            "HotelPhotoURL": "string"
        },
        "Doc": {
            "GuestType": "number",
            "DocType": "number",
            "DocNo": "string",
            "DocName": "string",
            "GuestName": "string",
            "BornDate": "string",
            "Sex": "number",
            "NativePlace": "string",
            "Nation": "string",
            "AuthStatus": "number",
            "ResAddress": "string",
            "State": "number",
            "CertiOffice": "string",
            "CertiEffStartTime": "long",
            "CertiEffEndTime": "long",
            "DocPhotoURL": "string",
            "Remark": "string"
        },
        "IDAuthenticationResult": {
            "DocNo": "string",
            "DocType": "string",
            "DocName": "string",
            "MatchPercent": "int",
            "MatchPass": "string",
            "IDCardImage": "string",
            "MatchImage": "string"
        }
    }],
    "ACT": "int"
};