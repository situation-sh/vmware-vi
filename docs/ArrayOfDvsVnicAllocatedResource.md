# ArrayOfDvsVnicAllocatedResource

A boxed array of *DvsVnicAllocatedResource*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsVnicAllocatedResource]**](DvsVnicAllocatedResource.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_vnic_allocated_resource import ArrayOfDvsVnicAllocatedResource

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsVnicAllocatedResource from a JSON string
array_of_dvs_vnic_allocated_resource_instance = ArrayOfDvsVnicAllocatedResource.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsVnicAllocatedResource.to_json()

# convert the object into a dict
array_of_dvs_vnic_allocated_resource_dict = array_of_dvs_vnic_allocated_resource_instance.to_dict()
# create an instance of ArrayOfDvsVnicAllocatedResource from a dict
array_of_dvs_vnic_allocated_resource_form_dict = array_of_dvs_vnic_allocated_resource.from_dict(array_of_dvs_vnic_allocated_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


