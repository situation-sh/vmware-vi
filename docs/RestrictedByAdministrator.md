# RestrictedByAdministrator

This fault is thrown when an operation cannot complete because of some restriction set by the server administrator.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **str** |  | 

## Example

```python
from vmware_vi.models.restricted_by_administrator import RestrictedByAdministrator

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictedByAdministrator from a JSON string
restricted_by_administrator_instance = RestrictedByAdministrator.from_json(json)
# print the JSON string representation of the object
print RestrictedByAdministrator.to_json()

# convert the object into a dict
restricted_by_administrator_dict = restricted_by_administrator_instance.to_dict()
# create an instance of RestrictedByAdministrator from a dict
restricted_by_administrator_form_dict = restricted_by_administrator.from_dict(restricted_by_administrator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


