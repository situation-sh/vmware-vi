# QueryConnectionInfoRequestType

The parameters of *Datacenter.QueryConnectionInfo*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | The target of the query.  | 
**port** | **int** | The port number of the target host. For ESX 2.x this is the authd port (902 by default). For ESX 3.x and above and for VMware Server hosts this is the https port (443 by default). You can specify -1 to have the vCenter Server try the default ports.  | 
**username** | **str** | The name of the user.  | 
**password** | **str** | The password of the user.  | 
**ssl_thumbprint** | **str** | The expected SSL thumbprint of the host&#39;s certificate.  | [optional] 

## Example

```python
from vmware_vi.models.query_connection_info_request_type import QueryConnectionInfoRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryConnectionInfoRequestType from a JSON string
query_connection_info_request_type_instance = QueryConnectionInfoRequestType.from_json(json)
# print the JSON string representation of the object
print QueryConnectionInfoRequestType.to_json()

# convert the object into a dict
query_connection_info_request_type_dict = query_connection_info_request_type_instance.to_dict()
# create an instance of QueryConnectionInfoRequestType from a dict
query_connection_info_request_type_form_dict = query_connection_info_request_type.from_dict(query_connection_info_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


