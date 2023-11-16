# ClusterDrsRecommendation

Deprecated as of VI API 2.5 use *ClusterRecommendation*.  DrsRecommendation describes a recommendation to migrate one or more virtual machines. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key to identify the recommendation when calling applyRecommendation.  | 
**rating** | **int** | A rating of the recommendation.  Valid values range from 1 (lowest confidence) to 5 (highest confidence).  | 
**reason** | **str** | A reason code explaining why this set of migrations is being suggested.  | 
**reason_text** | **str** | Text that provides more information about the reason code for the suggested set of migrations.  | 
**migration_list** | [**List[ClusterDrsMigration]**](ClusterDrsMigration.md) | Deprecated a more general *recommendation* list should be used. This recommendation type and the migrationList is kept for backward compatibility.  List of migrations in this recommendation and all the parent recommendations on which this recommendation depends.  All the migrations in this list can be constructed from *ClusterRecommendation.prerequisite* and *ClusterRecommendation.action*.  | 

## Example

```python
from vmware_vi.models.cluster_drs_recommendation import ClusterDrsRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDrsRecommendation from a JSON string
cluster_drs_recommendation_instance = ClusterDrsRecommendation.from_json(json)
# print the JSON string representation of the object
print ClusterDrsRecommendation.to_json()

# convert the object into a dict
cluster_drs_recommendation_dict = cluster_drs_recommendation_instance.to_dict()
# create an instance of ClusterDrsRecommendation from a dict
cluster_drs_recommendation_form_dict = cluster_drs_recommendation.from_dict(cluster_drs_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


