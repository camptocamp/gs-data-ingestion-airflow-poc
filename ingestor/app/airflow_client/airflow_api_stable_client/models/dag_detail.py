import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cron_expression_type_0 import CronExpressionType0
    from ..models.dag_detail_dataset_expression_type_0 import DAGDetailDatasetExpressionType0
    from ..models.dag_detail_params import DAGDetailParams
    from ..models.relative_delta import RelativeDelta
    from ..models.tag import Tag
    from ..models.time_delta_type_0 import TimeDeltaType0


T = TypeVar("T", bound="DAGDetail")


@_attrs_define
class DAGDetail:
    """DAG details.

    For details see:
    [airflow.models.dag.DAG](https://airflow.apache.org/docs/apache-
    airflow/stable/_api/airflow/models/dag/index.html#airflow.models.dag.DAG)

        Attributes:
            dag_id (Union[Unset, str]): The ID of the DAG.
            dag_display_name (Union[Unset, str]): Human centric display text for the DAG.

                *New in version 2.9.0*
            root_dag_id (Union[None, Unset, str]): If the DAG is SubDAG then it is the top level DAG identifier. Otherwise,
                null.
            is_paused (Union[None, Unset, bool]): Whether the DAG is paused.
            is_active (Union[None, Unset, bool]): Whether the DAG is currently seen by the scheduler(s).

                *New in version 2.1.1*

                *Changed in version 2.2.0*&#58; Field is read-only.
            is_subdag (Union[Unset, bool]): Whether the DAG is SubDAG.
            last_parsed_time (Union[None, Unset, datetime.datetime]): The last time the DAG was parsed.

                *New in version 2.3.0*
            last_pickled (Union[None, Unset, datetime.datetime]): The last time the DAG was pickled.

                *New in version 2.3.0*
            last_expired (Union[None, Unset, datetime.datetime]): Time when the DAG last received a refresh signal
                (e.g. the DAG's "refresh" button was clicked in the web UI)

                *New in version 2.3.0*
            scheduler_lock (Union[None, Unset, bool]): Whether (one of) the scheduler is scheduling this DAG at the moment

                *New in version 2.3.0*
            pickle_id (Union[None, Unset, str]): Foreign key to the latest pickle_id

                *New in version 2.3.0*
            default_view (Union[None, Unset, str]): Default view of the DAG inside the webserver

                *New in version 2.3.0*
            fileloc (Union[Unset, str]): The absolute path to the file.
            file_token (Union[Unset, str]): The key containing the encrypted path to the file. Encryption and decryption
                take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API
                extensibility, because the format of encrypted data may change.
            owners (Union[Unset, List[str]]):
            description (Union[None, Unset, str]): User-provided DAG description, which can consist of several sentences or
                paragraphs that describe DAG contents.
            schedule_interval (Union['CronExpressionType0', 'RelativeDelta', 'TimeDeltaType0', None, Unset]): Schedule
                interval. Defines how often DAG runs, this object gets added to your latest task instance's
                execution_date to figure out the next schedule.
            timetable_description (Union[None, Unset, str]): Timetable/Schedule Interval description.

                *New in version 2.3.0*
            tags (Union[List['Tag'], None, Unset]): List of tags.
            max_active_tasks (Union[None, Unset, int]): Maximum number of active tasks that can be run on the DAG

                *New in version 2.3.0*
            max_active_runs (Union[None, Unset, int]): Maximum number of active DAG runs for the DAG

                *New in version 2.3.0*
            has_task_concurrency_limits (Union[None, Unset, bool]): Whether the DAG has task concurrency limits

                *New in version 2.3.0*
            has_import_errors (Union[None, Unset, bool]): Whether the DAG has import errors

                *New in version 2.3.0*
            next_dagrun (Union[None, Unset, datetime.datetime]): The logical date of the next dag run.

                *New in version 2.3.0*
            next_dagrun_data_interval_start (Union[None, Unset, datetime.datetime]): The start of the interval of the next
                dag run.

                *New in version 2.3.0*
            next_dagrun_data_interval_end (Union[None, Unset, datetime.datetime]): The end of the interval of the next dag
                run.

                *New in version 2.3.0*
            next_dagrun_create_after (Union[None, Unset, datetime.datetime]): Earliest time at which this ``next_dagrun``
                can be created.

                *New in version 2.3.0*
            max_consecutive_failed_dag_runs (Union[None, Unset, int]): (experimental) The maximum number of consecutive DAG
                failures before DAG is automatically paused.

                *New in version 2.9.0*
            timezone (Union[Unset, str]):
            catchup (Union[None, Unset, bool]):
            orientation (Union[None, Unset, str]):
            concurrency (Union[None, Unset, float]):
            start_date (Union[None, Unset, datetime.datetime]): The DAG's start date.

                *Changed in version 2.0.1*&#58; Field becomes nullable.
            dag_run_timeout (Union['TimeDeltaType0', None, Unset]): Time delta
            dataset_expression (Union['DAGDetailDatasetExpressionType0', None, Unset]): Nested dataset any/all conditions
            doc_md (Union[None, Unset, str]):
            params (Union[Unset, DAGDetailParams]): User-specified DAG params.

                *New in version 2.0.1*
            end_date (Union[None, Unset, datetime.datetime]): The DAG's end date.

                *New in version 2.3.0*.
            is_paused_upon_creation (Union[None, Unset, bool]): Whether the DAG is paused upon creation.

                *New in version 2.3.0*
            last_parsed (Union[None, Unset, datetime.datetime]): The last time the DAG was parsed.

                *New in version 2.3.0*
            template_search_path (Union[List[str], None, Unset]): The template search path.

                *New in version 2.3.0*
            render_template_as_native_obj (Union[None, Unset, bool]): Whether to render templates as native Python objects.

                *New in version 2.3.0*
    """

    dag_id: Union[Unset, str] = UNSET
    dag_display_name: Union[Unset, str] = UNSET
    root_dag_id: Union[None, Unset, str] = UNSET
    is_paused: Union[None, Unset, bool] = UNSET
    is_active: Union[None, Unset, bool] = UNSET
    is_subdag: Union[Unset, bool] = UNSET
    last_parsed_time: Union[None, Unset, datetime.datetime] = UNSET
    last_pickled: Union[None, Unset, datetime.datetime] = UNSET
    last_expired: Union[None, Unset, datetime.datetime] = UNSET
    scheduler_lock: Union[None, Unset, bool] = UNSET
    pickle_id: Union[None, Unset, str] = UNSET
    default_view: Union[None, Unset, str] = UNSET
    fileloc: Union[Unset, str] = UNSET
    file_token: Union[Unset, str] = UNSET
    owners: Union[Unset, List[str]] = UNSET
    description: Union[None, Unset, str] = UNSET
    schedule_interval: Union["CronExpressionType0", "RelativeDelta", "TimeDeltaType0", None, Unset] = UNSET
    timetable_description: Union[None, Unset, str] = UNSET
    tags: Union[List["Tag"], None, Unset] = UNSET
    max_active_tasks: Union[None, Unset, int] = UNSET
    max_active_runs: Union[None, Unset, int] = UNSET
    has_task_concurrency_limits: Union[None, Unset, bool] = UNSET
    has_import_errors: Union[None, Unset, bool] = UNSET
    next_dagrun: Union[None, Unset, datetime.datetime] = UNSET
    next_dagrun_data_interval_start: Union[None, Unset, datetime.datetime] = UNSET
    next_dagrun_data_interval_end: Union[None, Unset, datetime.datetime] = UNSET
    next_dagrun_create_after: Union[None, Unset, datetime.datetime] = UNSET
    max_consecutive_failed_dag_runs: Union[None, Unset, int] = UNSET
    timezone: Union[Unset, str] = UNSET
    catchup: Union[None, Unset, bool] = UNSET
    orientation: Union[None, Unset, str] = UNSET
    concurrency: Union[None, Unset, float] = UNSET
    start_date: Union[None, Unset, datetime.datetime] = UNSET
    dag_run_timeout: Union["TimeDeltaType0", None, Unset] = UNSET
    dataset_expression: Union["DAGDetailDatasetExpressionType0", None, Unset] = UNSET
    doc_md: Union[None, Unset, str] = UNSET
    params: Union[Unset, "DAGDetailParams"] = UNSET
    end_date: Union[None, Unset, datetime.datetime] = UNSET
    is_paused_upon_creation: Union[None, Unset, bool] = UNSET
    last_parsed: Union[None, Unset, datetime.datetime] = UNSET
    template_search_path: Union[List[str], None, Unset] = UNSET
    render_template_as_native_obj: Union[None, Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.cron_expression_type_0 import CronExpressionType0
        from ..models.dag_detail_dataset_expression_type_0 import DAGDetailDatasetExpressionType0
        from ..models.relative_delta import RelativeDelta
        from ..models.time_delta_type_0 import TimeDeltaType0

        dag_id = self.dag_id

        dag_display_name = self.dag_display_name

        root_dag_id: Union[None, Unset, str]
        if isinstance(self.root_dag_id, Unset):
            root_dag_id = UNSET
        else:
            root_dag_id = self.root_dag_id

        is_paused: Union[None, Unset, bool]
        if isinstance(self.is_paused, Unset):
            is_paused = UNSET
        else:
            is_paused = self.is_paused

        is_active: Union[None, Unset, bool]
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        is_subdag = self.is_subdag

        last_parsed_time: Union[None, Unset, str]
        if isinstance(self.last_parsed_time, Unset):
            last_parsed_time = UNSET
        elif isinstance(self.last_parsed_time, datetime.datetime):
            last_parsed_time = self.last_parsed_time.isoformat()
        else:
            last_parsed_time = self.last_parsed_time

        last_pickled: Union[None, Unset, str]
        if isinstance(self.last_pickled, Unset):
            last_pickled = UNSET
        elif isinstance(self.last_pickled, datetime.datetime):
            last_pickled = self.last_pickled.isoformat()
        else:
            last_pickled = self.last_pickled

        last_expired: Union[None, Unset, str]
        if isinstance(self.last_expired, Unset):
            last_expired = UNSET
        elif isinstance(self.last_expired, datetime.datetime):
            last_expired = self.last_expired.isoformat()
        else:
            last_expired = self.last_expired

        scheduler_lock: Union[None, Unset, bool]
        if isinstance(self.scheduler_lock, Unset):
            scheduler_lock = UNSET
        else:
            scheduler_lock = self.scheduler_lock

        pickle_id: Union[None, Unset, str]
        if isinstance(self.pickle_id, Unset):
            pickle_id = UNSET
        else:
            pickle_id = self.pickle_id

        default_view: Union[None, Unset, str]
        if isinstance(self.default_view, Unset):
            default_view = UNSET
        else:
            default_view = self.default_view

        fileloc = self.fileloc

        file_token = self.file_token

        owners: Union[Unset, List[str]] = UNSET
        if not isinstance(self.owners, Unset):
            owners = self.owners

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        schedule_interval: Union[Dict[str, Any], None, Unset]
        if isinstance(self.schedule_interval, Unset):
            schedule_interval = UNSET
        elif isinstance(self.schedule_interval, TimeDeltaType0):
            schedule_interval = self.schedule_interval.to_dict()
        elif isinstance(self.schedule_interval, RelativeDelta):
            schedule_interval = self.schedule_interval.to_dict()
        elif isinstance(self.schedule_interval, CronExpressionType0):
            schedule_interval = self.schedule_interval.to_dict()
        else:
            schedule_interval = self.schedule_interval

        timetable_description: Union[None, Unset, str]
        if isinstance(self.timetable_description, Unset):
            timetable_description = UNSET
        else:
            timetable_description = self.timetable_description

        tags: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        max_active_tasks: Union[None, Unset, int]
        if isinstance(self.max_active_tasks, Unset):
            max_active_tasks = UNSET
        else:
            max_active_tasks = self.max_active_tasks

        max_active_runs: Union[None, Unset, int]
        if isinstance(self.max_active_runs, Unset):
            max_active_runs = UNSET
        else:
            max_active_runs = self.max_active_runs

        has_task_concurrency_limits: Union[None, Unset, bool]
        if isinstance(self.has_task_concurrency_limits, Unset):
            has_task_concurrency_limits = UNSET
        else:
            has_task_concurrency_limits = self.has_task_concurrency_limits

        has_import_errors: Union[None, Unset, bool]
        if isinstance(self.has_import_errors, Unset):
            has_import_errors = UNSET
        else:
            has_import_errors = self.has_import_errors

        next_dagrun: Union[None, Unset, str]
        if isinstance(self.next_dagrun, Unset):
            next_dagrun = UNSET
        elif isinstance(self.next_dagrun, datetime.datetime):
            next_dagrun = self.next_dagrun.isoformat()
        else:
            next_dagrun = self.next_dagrun

        next_dagrun_data_interval_start: Union[None, Unset, str]
        if isinstance(self.next_dagrun_data_interval_start, Unset):
            next_dagrun_data_interval_start = UNSET
        elif isinstance(self.next_dagrun_data_interval_start, datetime.datetime):
            next_dagrun_data_interval_start = self.next_dagrun_data_interval_start.isoformat()
        else:
            next_dagrun_data_interval_start = self.next_dagrun_data_interval_start

        next_dagrun_data_interval_end: Union[None, Unset, str]
        if isinstance(self.next_dagrun_data_interval_end, Unset):
            next_dagrun_data_interval_end = UNSET
        elif isinstance(self.next_dagrun_data_interval_end, datetime.datetime):
            next_dagrun_data_interval_end = self.next_dagrun_data_interval_end.isoformat()
        else:
            next_dagrun_data_interval_end = self.next_dagrun_data_interval_end

        next_dagrun_create_after: Union[None, Unset, str]
        if isinstance(self.next_dagrun_create_after, Unset):
            next_dagrun_create_after = UNSET
        elif isinstance(self.next_dagrun_create_after, datetime.datetime):
            next_dagrun_create_after = self.next_dagrun_create_after.isoformat()
        else:
            next_dagrun_create_after = self.next_dagrun_create_after

        max_consecutive_failed_dag_runs: Union[None, Unset, int]
        if isinstance(self.max_consecutive_failed_dag_runs, Unset):
            max_consecutive_failed_dag_runs = UNSET
        else:
            max_consecutive_failed_dag_runs = self.max_consecutive_failed_dag_runs

        timezone = self.timezone

        catchup: Union[None, Unset, bool]
        if isinstance(self.catchup, Unset):
            catchup = UNSET
        else:
            catchup = self.catchup

        orientation: Union[None, Unset, str]
        if isinstance(self.orientation, Unset):
            orientation = UNSET
        else:
            orientation = self.orientation

        concurrency: Union[None, Unset, float]
        if isinstance(self.concurrency, Unset):
            concurrency = UNSET
        else:
            concurrency = self.concurrency

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        dag_run_timeout: Union[Dict[str, Any], None, Unset]
        if isinstance(self.dag_run_timeout, Unset):
            dag_run_timeout = UNSET
        elif isinstance(self.dag_run_timeout, TimeDeltaType0):
            dag_run_timeout = self.dag_run_timeout.to_dict()
        else:
            dag_run_timeout = self.dag_run_timeout

        dataset_expression: Union[Dict[str, Any], None, Unset]
        if isinstance(self.dataset_expression, Unset):
            dataset_expression = UNSET
        elif isinstance(self.dataset_expression, DAGDetailDatasetExpressionType0):
            dataset_expression = self.dataset_expression.to_dict()
        else:
            dataset_expression = self.dataset_expression

        doc_md: Union[None, Unset, str]
        if isinstance(self.doc_md, Unset):
            doc_md = UNSET
        else:
            doc_md = self.doc_md

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        is_paused_upon_creation: Union[None, Unset, bool]
        if isinstance(self.is_paused_upon_creation, Unset):
            is_paused_upon_creation = UNSET
        else:
            is_paused_upon_creation = self.is_paused_upon_creation

        last_parsed: Union[None, Unset, str]
        if isinstance(self.last_parsed, Unset):
            last_parsed = UNSET
        elif isinstance(self.last_parsed, datetime.datetime):
            last_parsed = self.last_parsed.isoformat()
        else:
            last_parsed = self.last_parsed

        template_search_path: Union[List[str], None, Unset]
        if isinstance(self.template_search_path, Unset):
            template_search_path = UNSET
        elif isinstance(self.template_search_path, list):
            template_search_path = self.template_search_path

        else:
            template_search_path = self.template_search_path

        render_template_as_native_obj: Union[None, Unset, bool]
        if isinstance(self.render_template_as_native_obj, Unset):
            render_template_as_native_obj = UNSET
        else:
            render_template_as_native_obj = self.render_template_as_native_obj

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if dag_display_name is not UNSET:
            field_dict["dag_display_name"] = dag_display_name
        if root_dag_id is not UNSET:
            field_dict["root_dag_id"] = root_dag_id
        if is_paused is not UNSET:
            field_dict["is_paused"] = is_paused
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_subdag is not UNSET:
            field_dict["is_subdag"] = is_subdag
        if last_parsed_time is not UNSET:
            field_dict["last_parsed_time"] = last_parsed_time
        if last_pickled is not UNSET:
            field_dict["last_pickled"] = last_pickled
        if last_expired is not UNSET:
            field_dict["last_expired"] = last_expired
        if scheduler_lock is not UNSET:
            field_dict["scheduler_lock"] = scheduler_lock
        if pickle_id is not UNSET:
            field_dict["pickle_id"] = pickle_id
        if default_view is not UNSET:
            field_dict["default_view"] = default_view
        if fileloc is not UNSET:
            field_dict["fileloc"] = fileloc
        if file_token is not UNSET:
            field_dict["file_token"] = file_token
        if owners is not UNSET:
            field_dict["owners"] = owners
        if description is not UNSET:
            field_dict["description"] = description
        if schedule_interval is not UNSET:
            field_dict["schedule_interval"] = schedule_interval
        if timetable_description is not UNSET:
            field_dict["timetable_description"] = timetable_description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if max_active_tasks is not UNSET:
            field_dict["max_active_tasks"] = max_active_tasks
        if max_active_runs is not UNSET:
            field_dict["max_active_runs"] = max_active_runs
        if has_task_concurrency_limits is not UNSET:
            field_dict["has_task_concurrency_limits"] = has_task_concurrency_limits
        if has_import_errors is not UNSET:
            field_dict["has_import_errors"] = has_import_errors
        if next_dagrun is not UNSET:
            field_dict["next_dagrun"] = next_dagrun
        if next_dagrun_data_interval_start is not UNSET:
            field_dict["next_dagrun_data_interval_start"] = next_dagrun_data_interval_start
        if next_dagrun_data_interval_end is not UNSET:
            field_dict["next_dagrun_data_interval_end"] = next_dagrun_data_interval_end
        if next_dagrun_create_after is not UNSET:
            field_dict["next_dagrun_create_after"] = next_dagrun_create_after
        if max_consecutive_failed_dag_runs is not UNSET:
            field_dict["max_consecutive_failed_dag_runs"] = max_consecutive_failed_dag_runs
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if catchup is not UNSET:
            field_dict["catchup"] = catchup
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if concurrency is not UNSET:
            field_dict["concurrency"] = concurrency
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if dag_run_timeout is not UNSET:
            field_dict["dag_run_timeout"] = dag_run_timeout
        if dataset_expression is not UNSET:
            field_dict["dataset_expression"] = dataset_expression
        if doc_md is not UNSET:
            field_dict["doc_md"] = doc_md
        if params is not UNSET:
            field_dict["params"] = params
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if is_paused_upon_creation is not UNSET:
            field_dict["is_paused_upon_creation"] = is_paused_upon_creation
        if last_parsed is not UNSET:
            field_dict["last_parsed"] = last_parsed
        if template_search_path is not UNSET:
            field_dict["template_search_path"] = template_search_path
        if render_template_as_native_obj is not UNSET:
            field_dict["render_template_as_native_obj"] = render_template_as_native_obj

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cron_expression_type_0 import CronExpressionType0
        from ..models.dag_detail_dataset_expression_type_0 import DAGDetailDatasetExpressionType0
        from ..models.dag_detail_params import DAGDetailParams
        from ..models.relative_delta import RelativeDelta
        from ..models.tag import Tag
        from ..models.time_delta_type_0 import TimeDeltaType0

        d = src_dict.copy()
        dag_id = d.pop("dag_id", UNSET)

        dag_display_name = d.pop("dag_display_name", UNSET)

        def _parse_root_dag_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        root_dag_id = _parse_root_dag_id(d.pop("root_dag_id", UNSET))

        def _parse_is_paused(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_paused = _parse_is_paused(d.pop("is_paused", UNSET))

        def _parse_is_active(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        is_subdag = d.pop("is_subdag", UNSET)

        def _parse_last_parsed_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_parsed_time_type_0 = isoparse(data)

                return last_parsed_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_parsed_time = _parse_last_parsed_time(d.pop("last_parsed_time", UNSET))

        def _parse_last_pickled(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_pickled_type_0 = isoparse(data)

                return last_pickled_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_pickled = _parse_last_pickled(d.pop("last_pickled", UNSET))

        def _parse_last_expired(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_expired_type_0 = isoparse(data)

                return last_expired_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_expired = _parse_last_expired(d.pop("last_expired", UNSET))

        def _parse_scheduler_lock(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        scheduler_lock = _parse_scheduler_lock(d.pop("scheduler_lock", UNSET))

        def _parse_pickle_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pickle_id = _parse_pickle_id(d.pop("pickle_id", UNSET))

        def _parse_default_view(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_view = _parse_default_view(d.pop("default_view", UNSET))

        fileloc = d.pop("fileloc", UNSET)

        file_token = d.pop("file_token", UNSET)

        owners = cast(List[str], d.pop("owners", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_schedule_interval(
            data: object,
        ) -> Union["CronExpressionType0", "RelativeDelta", "TimeDeltaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_time_delta_type_0 = TimeDeltaType0.from_dict(data)

                return componentsschemas_time_delta_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schedule_interval_type_1 = RelativeDelta.from_dict(data)

                return componentsschemas_schedule_interval_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_cron_expression_type_0 = CronExpressionType0.from_dict(data)

                return componentsschemas_cron_expression_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CronExpressionType0", "RelativeDelta", "TimeDeltaType0", None, Unset], data)

        schedule_interval = _parse_schedule_interval(d.pop("schedule_interval", UNSET))

        def _parse_timetable_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        timetable_description = _parse_timetable_description(d.pop("timetable_description", UNSET))

        def _parse_tags(data: object) -> Union[List["Tag"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = Tag.from_dict(tags_type_0_item_data)

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Tag"], None, Unset], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_max_active_tasks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_active_tasks = _parse_max_active_tasks(d.pop("max_active_tasks", UNSET))

        def _parse_max_active_runs(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_active_runs = _parse_max_active_runs(d.pop("max_active_runs", UNSET))

        def _parse_has_task_concurrency_limits(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_task_concurrency_limits = _parse_has_task_concurrency_limits(d.pop("has_task_concurrency_limits", UNSET))

        def _parse_has_import_errors(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_import_errors = _parse_has_import_errors(d.pop("has_import_errors", UNSET))

        def _parse_next_dagrun(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_type_0 = isoparse(data)

                return next_dagrun_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        next_dagrun = _parse_next_dagrun(d.pop("next_dagrun", UNSET))

        def _parse_next_dagrun_data_interval_start(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_data_interval_start_type_0 = isoparse(data)

                return next_dagrun_data_interval_start_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        next_dagrun_data_interval_start = _parse_next_dagrun_data_interval_start(
            d.pop("next_dagrun_data_interval_start", UNSET)
        )

        def _parse_next_dagrun_data_interval_end(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_data_interval_end_type_0 = isoparse(data)

                return next_dagrun_data_interval_end_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        next_dagrun_data_interval_end = _parse_next_dagrun_data_interval_end(
            d.pop("next_dagrun_data_interval_end", UNSET)
        )

        def _parse_next_dagrun_create_after(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_create_after_type_0 = isoparse(data)

                return next_dagrun_create_after_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        next_dagrun_create_after = _parse_next_dagrun_create_after(d.pop("next_dagrun_create_after", UNSET))

        def _parse_max_consecutive_failed_dag_runs(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_consecutive_failed_dag_runs = _parse_max_consecutive_failed_dag_runs(
            d.pop("max_consecutive_failed_dag_runs", UNSET)
        )

        timezone = d.pop("timezone", UNSET)

        def _parse_catchup(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        catchup = _parse_catchup(d.pop("catchup", UNSET))

        def _parse_orientation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        orientation = _parse_orientation(d.pop("orientation", UNSET))

        def _parse_concurrency(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        concurrency = _parse_concurrency(d.pop("concurrency", UNSET))

        def _parse_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_dag_run_timeout(data: object) -> Union["TimeDeltaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_time_delta_type_0 = TimeDeltaType0.from_dict(data)

                return componentsschemas_time_delta_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TimeDeltaType0", None, Unset], data)

        dag_run_timeout = _parse_dag_run_timeout(d.pop("dag_run_timeout", UNSET))

        def _parse_dataset_expression(data: object) -> Union["DAGDetailDatasetExpressionType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dataset_expression_type_0 = DAGDetailDatasetExpressionType0.from_dict(data)

                return dataset_expression_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DAGDetailDatasetExpressionType0", None, Unset], data)

        dataset_expression = _parse_dataset_expression(d.pop("dataset_expression", UNSET))

        def _parse_doc_md(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        doc_md = _parse_doc_md(d.pop("doc_md", UNSET))

        _params = d.pop("params", UNSET)
        params: Union[Unset, DAGDetailParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = DAGDetailParams.from_dict(_params)

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_is_paused_upon_creation(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_paused_upon_creation = _parse_is_paused_upon_creation(d.pop("is_paused_upon_creation", UNSET))

        def _parse_last_parsed(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_parsed_type_0 = isoparse(data)

                return last_parsed_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_parsed = _parse_last_parsed(d.pop("last_parsed", UNSET))

        def _parse_template_search_path(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                template_search_path_type_0 = cast(List[str], data)

                return template_search_path_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        template_search_path = _parse_template_search_path(d.pop("template_search_path", UNSET))

        def _parse_render_template_as_native_obj(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        render_template_as_native_obj = _parse_render_template_as_native_obj(
            d.pop("render_template_as_native_obj", UNSET)
        )

        dag_detail = cls(
            dag_id=dag_id,
            dag_display_name=dag_display_name,
            root_dag_id=root_dag_id,
            is_paused=is_paused,
            is_active=is_active,
            is_subdag=is_subdag,
            last_parsed_time=last_parsed_time,
            last_pickled=last_pickled,
            last_expired=last_expired,
            scheduler_lock=scheduler_lock,
            pickle_id=pickle_id,
            default_view=default_view,
            fileloc=fileloc,
            file_token=file_token,
            owners=owners,
            description=description,
            schedule_interval=schedule_interval,
            timetable_description=timetable_description,
            tags=tags,
            max_active_tasks=max_active_tasks,
            max_active_runs=max_active_runs,
            has_task_concurrency_limits=has_task_concurrency_limits,
            has_import_errors=has_import_errors,
            next_dagrun=next_dagrun,
            next_dagrun_data_interval_start=next_dagrun_data_interval_start,
            next_dagrun_data_interval_end=next_dagrun_data_interval_end,
            next_dagrun_create_after=next_dagrun_create_after,
            max_consecutive_failed_dag_runs=max_consecutive_failed_dag_runs,
            timezone=timezone,
            catchup=catchup,
            orientation=orientation,
            concurrency=concurrency,
            start_date=start_date,
            dag_run_timeout=dag_run_timeout,
            dataset_expression=dataset_expression,
            doc_md=doc_md,
            params=params,
            end_date=end_date,
            is_paused_upon_creation=is_paused_upon_creation,
            last_parsed=last_parsed,
            template_search_path=template_search_path,
            render_template_as_native_obj=render_template_as_native_obj,
        )

        dag_detail.additional_properties = d
        return dag_detail

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
