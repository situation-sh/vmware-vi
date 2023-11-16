# LicenseEntityNotFound

An LicenseEntityNotFound fault is thrown when an attempt is do any operation on an entity/licensed asset that does not exist.  Example, remove an entity that does not exist.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | 

## Example

```python
from vmware_vi.models.license_entity_not_found import LicenseEntityNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseEntityNotFound from a JSON string
license_entity_not_found_instance = LicenseEntityNotFound.from_json(json)
# print the JSON string representation of the object
print LicenseEntityNotFound.to_json()

# convert the object into a dict
license_entity_not_found_dict = license_entity_not_found_instance.to_dict()
# create an instance of LicenseEntityNotFound from a dict
license_entity_not_found_form_dict = license_entity_not_found.from_dict(license_entity_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


