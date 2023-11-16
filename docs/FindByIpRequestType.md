# FindByIpRequestType

The parameters of *SearchIndex.FindByIp*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**ip** | **str** | The dot-decimal notation formatted IP address to find.  | 
**vm_search** | **bool** | if true, search for virtual machines, otherwise search for hosts.  | 

## Example

```python
from vmware_vi.models.find_by_ip_request_type import FindByIpRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FindByIpRequestType from a JSON string
find_by_ip_request_type_instance = FindByIpRequestType.from_json(json)
# print the JSON string representation of the object
print FindByIpRequestType.to_json()

# convert the object into a dict
find_by_ip_request_type_dict = find_by_ip_request_type_instance.to_dict()
# create an instance of FindByIpRequestType from a dict
find_by_ip_request_type_form_dict = find_by_ip_request_type.from_dict(find_by_ip_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


