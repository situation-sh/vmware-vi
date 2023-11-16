# DatabaseSizeParam

DatabaseSizeParam contains information about a sample inventory.  Using this information, database size requirements for that sample inventory can be computed. Depending on the accuracy of estimate desired, users can choose to specify the number of different types of managed entities. The numHosts and numVirtualMachines are the only two required fields. Rest are all optional fields filled up by Virtual Center based on some heuristics. These parameters need not represent a real inventory. The user can use these parameters to estimate the database size required by a hypothetical VirtualCenter setup.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_desc** | [**InventoryDescription**](InventoryDescription.md) |  | 
**perf_stats_desc** | [**PerformanceStatisticsDescription**](PerformanceStatisticsDescription.md) |  | [optional] 

## Example

```python
from vmware_vi.models.database_size_param import DatabaseSizeParam

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseSizeParam from a JSON string
database_size_param_instance = DatabaseSizeParam.from_json(json)
# print the JSON string representation of the object
print DatabaseSizeParam.to_json()

# convert the object into a dict
database_size_param_dict = database_size_param_instance.to_dict()
# create an instance of DatabaseSizeParam from a dict
database_size_param_form_dict = database_size_param.from_dict(database_size_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


