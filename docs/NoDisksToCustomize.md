# NoDisksToCustomize

None of the disks attached to the VM are suitable for customization. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_disks_to_customize import NoDisksToCustomize

# TODO update the JSON string below
json = "{}"
# create an instance of NoDisksToCustomize from a JSON string
no_disks_to_customize_instance = NoDisksToCustomize.from_json(json)
# print the JSON string representation of the object
print NoDisksToCustomize.to_json()

# convert the object into a dict
no_disks_to_customize_dict = no_disks_to_customize_instance.to_dict()
# create an instance of NoDisksToCustomize from a dict
no_disks_to_customize_form_dict = no_disks_to_customize.from_dict(no_disks_to_customize_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


