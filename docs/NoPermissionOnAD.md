# NoPermissionOnAD

Fault indicating that the user account used to connect to the Active Directory doesn not have enough permissions for the action that was attempted.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_permission_on_ad import NoPermissionOnAD

# TODO update the JSON string below
json = "{}"
# create an instance of NoPermissionOnAD from a JSON string
no_permission_on_ad_instance = NoPermissionOnAD.from_json(json)
# print the JSON string representation of the object
print NoPermissionOnAD.to_json()

# convert the object into a dict
no_permission_on_ad_dict = no_permission_on_ad_instance.to_dict()
# create an instance of NoPermissionOnAD from a dict
no_permission_on_ad_form_dict = no_permission_on_ad.from_dict(no_permission_on_ad_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


