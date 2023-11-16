# ArrayOfIscsiFaultInvalidVnic

A boxed array of *IscsiFaultInvalidVnic*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IscsiFaultInvalidVnic]**](IscsiFaultInvalidVnic.md) |  | 

## Example

```python
from vmware_vi.models.array_of_iscsi_fault_invalid_vnic import ArrayOfIscsiFaultInvalidVnic

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIscsiFaultInvalidVnic from a JSON string
array_of_iscsi_fault_invalid_vnic_instance = ArrayOfIscsiFaultInvalidVnic.from_json(json)
# print the JSON string representation of the object
print ArrayOfIscsiFaultInvalidVnic.to_json()

# convert the object into a dict
array_of_iscsi_fault_invalid_vnic_dict = array_of_iscsi_fault_invalid_vnic_instance.to_dict()
# create an instance of ArrayOfIscsiFaultInvalidVnic from a dict
array_of_iscsi_fault_invalid_vnic_form_dict = array_of_iscsi_fault_invalid_vnic.from_dict(array_of_iscsi_fault_invalid_vnic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


