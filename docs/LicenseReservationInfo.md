# LicenseReservationInfo

Deprecated as of vSphere API 4.0, this is not used by the system.  A reservation describes how many licenses of a particular feature are being used by a particular feature. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of the License Feature.  See also *LicenseFeatureInfo.key*.  | 
**state** | [**LicenseReservationInfoStateEnum**](LicenseReservationInfoStateEnum.md) |  | 
**required** | **int** | Contains the required number of licenses of the particular type that the product needs in its current configuration.  Licenses are normally allocated at the same time as they are needed, so the value of required is set at the time the license is needed. For example, in the case of the number of licenses based on virtual machines, the required count is set at the time a virtual machine is powered on, just before the license is checked out.  | 

## Example

```python
from vmware_vi.models.license_reservation_info import LicenseReservationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseReservationInfo from a JSON string
license_reservation_info_instance = LicenseReservationInfo.from_json(json)
# print the JSON string representation of the object
print LicenseReservationInfo.to_json()

# convert the object into a dict
license_reservation_info_dict = license_reservation_info_instance.to_dict()
# create an instance of LicenseReservationInfo from a dict
license_reservation_info_form_dict = license_reservation_info.from_dict(license_reservation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


