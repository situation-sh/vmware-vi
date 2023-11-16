# LicenseReservationInfoState

A boxed *LicenseReservationInfoState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**LicenseReservationInfoStateEnum**](LicenseReservationInfoStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.license_reservation_info_state import LicenseReservationInfoState

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseReservationInfoState from a JSON string
license_reservation_info_state_instance = LicenseReservationInfoState.from_json(json)
# print the JSON string representation of the object
print LicenseReservationInfoState.to_json()

# convert the object into a dict
license_reservation_info_state_dict = license_reservation_info_state_instance.to_dict()
# create an instance of LicenseReservationInfoState from a dict
license_reservation_info_state_form_dict = license_reservation_info_state.from_dict(license_reservation_info_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


