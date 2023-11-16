# SelectActivePartitionRequestType

The parameters of *HostDiagnosticSystem.SelectActivePartition*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition** | [**HostScsiDiskPartition**](HostScsiDiskPartition.md) |  | [optional] 

## Example

```python
from vmware_vi.models.select_active_partition_request_type import SelectActivePartitionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SelectActivePartitionRequestType from a JSON string
select_active_partition_request_type_instance = SelectActivePartitionRequestType.from_json(json)
# print the JSON string representation of the object
print SelectActivePartitionRequestType.to_json()

# convert the object into a dict
select_active_partition_request_type_dict = select_active_partition_request_type_instance.to_dict()
# create an instance of SelectActivePartitionRequestType from a dict
select_active_partition_request_type_form_dict = select_active_partition_request_type.from_dict(select_active_partition_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


