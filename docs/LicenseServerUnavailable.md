# LicenseServerUnavailable

This fault is thrown when the License Server is unavailable during an attempt to change license state. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_server** | **str** | The name of the unavailable license server.  | 

## Example

```python
from vmware_vi.models.license_server_unavailable import LicenseServerUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseServerUnavailable from a JSON string
license_server_unavailable_instance = LicenseServerUnavailable.from_json(json)
# print the JSON string representation of the object
print LicenseServerUnavailable.to_json()

# convert the object into a dict
license_server_unavailable_dict = license_server_unavailable_instance.to_dict()
# create an instance of LicenseServerUnavailable from a dict
license_server_unavailable_form_dict = license_server_unavailable.from_dict(license_server_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


