# KmipServerSpec

Data Object representing a KMIP server connection spec.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | [**KeyProviderId**](KeyProviderId.md) |  | 
**info** | [**KmipServerInfo**](KmipServerInfo.md) |  | 
**password** | **str** | Password to authenticate to the KMIP server.  Set value to empty string to delete the entry.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.kmip_server_spec import KmipServerSpec

# TODO update the JSON string below
json = "{}"
# create an instance of KmipServerSpec from a JSON string
kmip_server_spec_instance = KmipServerSpec.from_json(json)
# print the JSON string representation of the object
print KmipServerSpec.to_json()

# convert the object into a dict
kmip_server_spec_dict = kmip_server_spec_instance.to_dict()
# create an instance of KmipServerSpec from a dict
kmip_server_spec_form_dict = kmip_server_spec.from_dict(kmip_server_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


