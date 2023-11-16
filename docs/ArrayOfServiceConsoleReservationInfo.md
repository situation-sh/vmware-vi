# ArrayOfServiceConsoleReservationInfo

A boxed array of *ServiceConsoleReservationInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ServiceConsoleReservationInfo]**](ServiceConsoleReservationInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_service_console_reservation_info import ArrayOfServiceConsoleReservationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfServiceConsoleReservationInfo from a JSON string
array_of_service_console_reservation_info_instance = ArrayOfServiceConsoleReservationInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfServiceConsoleReservationInfo.to_json()

# convert the object into a dict
array_of_service_console_reservation_info_dict = array_of_service_console_reservation_info_instance.to_dict()
# create an instance of ArrayOfServiceConsoleReservationInfo from a dict
array_of_service_console_reservation_info_form_dict = array_of_service_console_reservation_info.from_dict(array_of_service_console_reservation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


