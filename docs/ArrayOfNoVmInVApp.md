# ArrayOfNoVmInVApp

A boxed array of *NoVmInVApp*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NoVmInVApp]**](NoVmInVApp.md) |  | 

## Example

```python
from vmware_vi.models.array_of_no_vm_in_v_app import ArrayOfNoVmInVApp

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNoVmInVApp from a JSON string
array_of_no_vm_in_v_app_instance = ArrayOfNoVmInVApp.from_json(json)
# print the JSON string representation of the object
print ArrayOfNoVmInVApp.to_json()

# convert the object into a dict
array_of_no_vm_in_v_app_dict = array_of_no_vm_in_v_app_instance.to_dict()
# create an instance of ArrayOfNoVmInVApp from a dict
array_of_no_vm_in_v_app_form_dict = array_of_no_vm_in_v_app.from_dict(array_of_no_vm_in_v_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


