# ArrayOfDvsFault

A boxed array of *DvsFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsFault]**](DvsFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_fault import ArrayOfDvsFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsFault from a JSON string
array_of_dvs_fault_instance = ArrayOfDvsFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsFault.to_json()

# convert the object into a dict
array_of_dvs_fault_dict = array_of_dvs_fault_instance.to_dict()
# create an instance of ArrayOfDvsFault from a dict
array_of_dvs_fault_form_dict = array_of_dvs_fault.from_dict(array_of_dvs_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


