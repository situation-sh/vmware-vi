# ArrayOfHostNatService

A boxed array of *HostNatService*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNatService]**](HostNatService.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nat_service import ArrayOfHostNatService

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNatService from a JSON string
array_of_host_nat_service_instance = ArrayOfHostNatService.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNatService.to_json()

# convert the object into a dict
array_of_host_nat_service_dict = array_of_host_nat_service_instance.to_dict()
# create an instance of ArrayOfHostNatService from a dict
array_of_host_nat_service_form_dict = array_of_host_nat_service.from_dict(array_of_host_nat_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


