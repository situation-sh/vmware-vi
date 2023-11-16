# RebootRequired

This fault is thrown if a patch install fails because an installed nonchainable patch has not taken effect. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch** | **str** | The nonchainable patch installed.  | [optional] 

## Example

```python
from vmware_vi.models.reboot_required import RebootRequired

# TODO update the JSON string below
json = "{}"
# create an instance of RebootRequired from a JSON string
reboot_required_instance = RebootRequired.from_json(json)
# print the JSON string representation of the object
print RebootRequired.to_json()

# convert the object into a dict
reboot_required_dict = reboot_required_instance.to_dict()
# create an instance of RebootRequired from a dict
reboot_required_form_dict = reboot_required.from_dict(reboot_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


