# ArrayOfApplicationQuiesceFault

A boxed array of *ApplicationQuiesceFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ApplicationQuiesceFault]**](ApplicationQuiesceFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_application_quiesce_fault import ArrayOfApplicationQuiesceFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfApplicationQuiesceFault from a JSON string
array_of_application_quiesce_fault_instance = ArrayOfApplicationQuiesceFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfApplicationQuiesceFault.to_json()

# convert the object into a dict
array_of_application_quiesce_fault_dict = array_of_application_quiesce_fault_instance.to_dict()
# create an instance of ArrayOfApplicationQuiesceFault from a dict
array_of_application_quiesce_fault_form_dict = array_of_application_quiesce_fault.from_dict(array_of_application_quiesce_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


