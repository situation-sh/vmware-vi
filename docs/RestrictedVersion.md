# RestrictedVersion

Thrown when the caller is not permitted to perform the specified operation due to product versioning restrictions.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.restricted_version import RestrictedVersion

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictedVersion from a JSON string
restricted_version_instance = RestrictedVersion.from_json(json)
# print the JSON string representation of the object
print RestrictedVersion.to_json()

# convert the object into a dict
restricted_version_dict = restricted_version_instance.to_dict()
# create an instance of RestrictedVersion from a dict
restricted_version_form_dict = restricted_version.from_dict(restricted_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


