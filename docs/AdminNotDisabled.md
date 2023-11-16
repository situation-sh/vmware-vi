# AdminNotDisabled

Fault thrown if an attempt to enable the Administrator permission on a host of which the Administator permission is not disabled.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.admin_not_disabled import AdminNotDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of AdminNotDisabled from a JSON string
admin_not_disabled_instance = AdminNotDisabled.from_json(json)
# print the JSON string representation of the object
print AdminNotDisabled.to_json()

# convert the object into a dict
admin_not_disabled_dict = admin_not_disabled_instance.to_dict()
# create an instance of AdminNotDisabled from a dict
admin_not_disabled_form_dict = admin_not_disabled.from_dict(admin_not_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


