# ArrayOfIscsiFault

A boxed array of *IscsiFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IscsiFault]**](IscsiFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_iscsi_fault import ArrayOfIscsiFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIscsiFault from a JSON string
array_of_iscsi_fault_instance = ArrayOfIscsiFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfIscsiFault.to_json()

# convert the object into a dict
array_of_iscsi_fault_dict = array_of_iscsi_fault_instance.to_dict()
# create an instance of ArrayOfIscsiFault from a dict
array_of_iscsi_fault_form_dict = array_of_iscsi_fault.from_dict(array_of_iscsi_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


