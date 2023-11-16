# FileTransferInformation

Represents the information about a *GuestFileManager.InitiateFileTransferFromGuest* operation of *GuestFileManager* object.  The user can use the URL provided in url property to transfer the file from the guest. The user should send a HTTP GET request to the URL. Entire file content will be returned in the body of the response message.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**GuestFileAttributes**](GuestFileAttributes.md) |  | 
**size** | **int** | Total size of the file in bytes.  ***Since:*** vSphere API 5.0  | 
**url** | **str** | Specifies the URL to which the user has to send HTTP GET request.  Multiple GET requests cannot be sent to the URL simultaneously. URL will become invalid once a successful GET request is sent.       The host part of the URL is returned as &#39;\\*&#39; if the hostname to be used is the name of the server to which the call was made. For example, if the call is made to esx-svr-1.domain1.com, and the file is available for download from &#x60;https://esx-svr-1.domain1.com/guestFile?id&#x3D;1&amp;token&#x3D;1234&#x60;, the URL returned may be &#x60;https://&amp;#42;/guestFile?id&#x3D;1&amp;token&#x3D;1234&#x60;. The client replaces the asterisk with the server name on which it invoked the call.       The URL is valid only for 10 minutes from the time it is generated. Also, the URL becomes invalid whenever the virtual machine is powered off, suspended or unregistered.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.file_transfer_information import FileTransferInformation

# TODO update the JSON string below
json = "{}"
# create an instance of FileTransferInformation from a JSON string
file_transfer_information_instance = FileTransferInformation.from_json(json)
# print the JSON string representation of the object
print FileTransferInformation.to_json()

# convert the object into a dict
file_transfer_information_dict = file_transfer_information_instance.to_dict()
# create an instance of FileTransferInformation from a dict
file_transfer_information_form_dict = file_transfer_information.from_dict(file_transfer_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


