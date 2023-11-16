# ServiceConsoleReservationInfo

The ServiceConsoleReservationInfo data object type describes the amount of memory that is being reserved by the service console.  Memory reserved for use by the service console is a hard reservation that cannot be changed except across hardware restarts.  This memory that is reserved for the service console is used primarily to provide system management services. In addition, a small overhead is needed by each virtual machine on the service console.  The only property of the data object that can be changed directly is the serviceConsoleReservedCfg property. This property indicates how much memory should be reserved for the service console on the next boot. In most cases, this amount is the same as the current reservation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_console_reserved_cfg** | **int** | The amount of memory that should be reserved for the service console on the next boot.  | 
**service_console_reserved** | **int** | The amount of memory that is currently reserved for the service console.  | 
**unreserved** | **int** | The amount of memory that is not reserved for use by the service console.  | 

## Example

```python
from vmware_vi.models.service_console_reservation_info import ServiceConsoleReservationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConsoleReservationInfo from a JSON string
service_console_reservation_info_instance = ServiceConsoleReservationInfo.from_json(json)
# print the JSON string representation of the object
print ServiceConsoleReservationInfo.to_json()

# convert the object into a dict
service_console_reservation_info_dict = service_console_reservation_info_instance.to_dict()
# create an instance of ServiceConsoleReservationInfo from a dict
service_console_reservation_info_form_dict = service_console_reservation_info.from_dict(service_console_reservation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


