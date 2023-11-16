# NoVmInVApp

Attempting to power-on or power-off a vApp that contains no virtual machines.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_vm_in_v_app import NoVmInVApp

# TODO update the JSON string below
json = "{}"
# create an instance of NoVmInVApp from a JSON string
no_vm_in_v_app_instance = NoVmInVApp.from_json(json)
# print the JSON string representation of the object
print NoVmInVApp.to_json()

# convert the object into a dict
no_vm_in_v_app_dict = no_vm_in_v_app_instance.to_dict()
# create an instance of NoVmInVApp from a dict
no_vm_in_v_app_form_dict = no_vm_in_v_app.from_dict(no_vm_in_v_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


