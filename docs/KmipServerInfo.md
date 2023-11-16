# KmipServerInfo

Data Object representing a KMIP server connection information.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the KMIP server.  ***Since:*** vSphere API 6.5  | 
**address** | **str** | Address of the KMIP server.  ***Since:*** vSphere API 6.5  | 
**port** | **int** | Port of the KMIP server.  ***Since:*** vSphere API 6.5  | 
**proxy_address** | **str** | Address of the proxy server.  Set value to empty string to delete the entry.  ***Since:*** vSphere API 6.5  | [optional] 
**proxy_port** | **int** | Port of the proxy server.  Set value \&quot;-1\&quot; to delete the entry.  ***Since:*** vSphere API 6.5  | [optional] 
**reconnect** | **int** | Should auto-reconnect be done.  Set value \&quot;-1\&quot; to delete the entry.  ***Since:*** vSphere API 6.5  | [optional] 
**protocol** | **str** | KMIP library protocol handler, e.g.  KMIP1. Set value to empty string to delete the entry.  ***Since:*** vSphere API 6.5  | [optional] 
**nbio** | **int** | Non-blocking I/O required.  Set value \&quot;-1\&quot; to delete the entry.  ***Since:*** vSphere API 6.5  | [optional] 
**timeout** | **int** | I/O timeout in seconds (-1&#x3D;none,0&#x3D;infinite).  Set value \&quot;-1\&quot; to delete the entry.  ***Since:*** vSphere API 6.5  | [optional] 
**user_name** | **str** | Username to authenticate to the KMIP server.  Set value to empty string to delete the entry.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.kmip_server_info import KmipServerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KmipServerInfo from a JSON string
kmip_server_info_instance = KmipServerInfo.from_json(json)
# print the JSON string representation of the object
print KmipServerInfo.to_json()

# convert the object into a dict
kmip_server_info_dict = kmip_server_info_instance.to_dict()
# create an instance of KmipServerInfo from a dict
kmip_server_info_form_dict = kmip_server_info.from_dict(kmip_server_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


