# PrivilegeAvailability

This class defines whether a specific privilege is granted.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priv_id** | **str** | The privilege ID.  ***Since:*** vSphere API 5.5  | 
**is_granted** | **bool** | True if the privilege is granted.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.privilege_availability import PrivilegeAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of PrivilegeAvailability from a JSON string
privilege_availability_instance = PrivilegeAvailability.from_json(json)
# print the JSON string representation of the object
print PrivilegeAvailability.to_json()

# convert the object into a dict
privilege_availability_dict = privilege_availability_instance.to_dict()
# create an instance of PrivilegeAvailability from a dict
privilege_availability_form_dict = privilege_availability.from_dict(privilege_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


