# CannotAccessVmComponent

One of the virtual machine's components is not accessible on the execution host.  This is a base class. Subclasses will encode the type of component that is not accessible. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_access_vm_component import CannotAccessVmComponent

# TODO update the JSON string below
json = "{}"
# create an instance of CannotAccessVmComponent from a JSON string
cannot_access_vm_component_instance = CannotAccessVmComponent.from_json(json)
# print the JSON string representation of the object
print CannotAccessVmComponent.to_json()

# convert the object into a dict
cannot_access_vm_component_dict = cannot_access_vm_component_instance.to_dict()
# create an instance of CannotAccessVmComponent from a dict
cannot_access_vm_component_form_dict = cannot_access_vm_component.from_dict(cannot_access_vm_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


