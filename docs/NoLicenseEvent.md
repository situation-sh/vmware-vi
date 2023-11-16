# NoLicenseEvent

These are events reported by License Manager.  A NoLicenseEvent is reported if the required licenses could not be reserved. Each feature that is not fully licensed is reported. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | [**LicenseFeatureInfo**](LicenseFeatureInfo.md) |  | 

## Example

```python
from vmware_vi.models.no_license_event import NoLicenseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of NoLicenseEvent from a JSON string
no_license_event_instance = NoLicenseEvent.from_json(json)
# print the JSON string representation of the object
print NoLicenseEvent.to_json()

# convert the object into a dict
no_license_event_dict = no_license_event_instance.to_dict()
# create an instance of NoLicenseEvent from a dict
no_license_event_form_dict = no_license_event.from_dict(no_license_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


