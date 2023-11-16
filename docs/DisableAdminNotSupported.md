# DisableAdminNotSupported

Fault thrown when an attempt is made to move a disk with associated snapshots to a destination host.  If such a move were to occur, snapshots associated with the disk would be irrevocably lost. This is always an error.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.disable_admin_not_supported import DisableAdminNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of DisableAdminNotSupported from a JSON string
disable_admin_not_supported_instance = DisableAdminNotSupported.from_json(json)
# print the JSON string representation of the object
print DisableAdminNotSupported.to_json()

# convert the object into a dict
disable_admin_not_supported_dict = disable_admin_not_supported_instance.to_dict()
# create an instance of DisableAdminNotSupported from a dict
disable_admin_not_supported_form_dict = disable_admin_not_supported.from_dict(disable_admin_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


