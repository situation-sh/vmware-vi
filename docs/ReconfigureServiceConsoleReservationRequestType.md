# ReconfigureServiceConsoleReservationRequestType

The parameters of *HostMemorySystem.ReconfigureServiceConsoleReservation*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cfg_bytes** | **int** |  | 

## Example

```python
from vmware_vi.models.reconfigure_service_console_reservation_request_type import ReconfigureServiceConsoleReservationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureServiceConsoleReservationRequestType from a JSON string
reconfigure_service_console_reservation_request_type_instance = ReconfigureServiceConsoleReservationRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigureServiceConsoleReservationRequestType.to_json()

# convert the object into a dict
reconfigure_service_console_reservation_request_type_dict = reconfigure_service_console_reservation_request_type_instance.to_dict()
# create an instance of ReconfigureServiceConsoleReservationRequestType from a dict
reconfigure_service_console_reservation_request_type_form_dict = reconfigure_service_console_reservation_request_type.from_dict(reconfigure_service_console_reservation_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


