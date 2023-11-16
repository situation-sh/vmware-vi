# ArrayOfVAppConfigFault

A boxed array of *VAppConfigFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VAppConfigFault]**](VAppConfigFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_app_config_fault import ArrayOfVAppConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVAppConfigFault from a JSON string
array_of_v_app_config_fault_instance = ArrayOfVAppConfigFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfVAppConfigFault.to_json()

# convert the object into a dict
array_of_v_app_config_fault_dict = array_of_v_app_config_fault_instance.to_dict()
# create an instance of ArrayOfVAppConfigFault from a dict
array_of_v_app_config_fault_form_dict = array_of_v_app_config_fault.from_dict(array_of_v_app_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


