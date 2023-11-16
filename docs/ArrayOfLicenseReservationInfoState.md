# ArrayOfLicenseReservationInfoState

A boxed array of *LicenseReservationInfoState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseReservationInfoStateEnum]**](LicenseReservationInfoStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_reservation_info_state import ArrayOfLicenseReservationInfoState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseReservationInfoState from a JSON string
array_of_license_reservation_info_state_instance = ArrayOfLicenseReservationInfoState.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseReservationInfoState.to_json()

# convert the object into a dict
array_of_license_reservation_info_state_dict = array_of_license_reservation_info_state_instance.to_dict()
# create an instance of ArrayOfLicenseReservationInfoState from a dict
array_of_license_reservation_info_state_form_dict = array_of_license_reservation_info_state.from_dict(array_of_license_reservation_info_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


