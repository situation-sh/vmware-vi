# AdminDisabled

Fault thrown if an attempt to disable the Administrator permission on a host of which the Administator permission has already been disabled.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.admin_disabled import AdminDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of AdminDisabled from a JSON string
admin_disabled_instance = AdminDisabled.from_json(json)
# print the JSON string representation of the object
print AdminDisabled.to_json()

# convert the object into a dict
admin_disabled_dict = admin_disabled_instance.to_dict()
# create an instance of AdminDisabled from a dict
admin_disabled_form_dict = admin_disabled.from_dict(admin_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


