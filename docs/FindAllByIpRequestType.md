# FindAllByIpRequestType

The parameters of *SearchIndex.FindAllByIp*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**ip** | **str** | The dot-decimal notation formatted IP address to find.  | 
**vm_search** | **bool** | If true, search for virtual machines, otherwise search for hosts.  | 

## Example

```python
from vmware_vi.models.find_all_by_ip_request_type import FindAllByIpRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FindAllByIpRequestType from a JSON string
find_all_by_ip_request_type_instance = FindAllByIpRequestType.from_json(json)
# print the JSON string representation of the object
print FindAllByIpRequestType.to_json()

# convert the object into a dict
find_all_by_ip_request_type_dict = find_all_by_ip_request_type_instance.to_dict()
# create an instance of FindAllByIpRequestType from a dict
find_all_by_ip_request_type_form_dict = find_all_by_ip_request_type.from_dict(find_all_by_ip_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


