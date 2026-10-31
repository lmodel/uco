package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A geolocation track facet is a grouping of characteristics unique to a set of contiguous geolocation entries representing a path/track taken.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeoLocationTrackFacet extends Facet {

  private ObservableObject application;
  private List<ObservableObject> geoLocationEntry;
  private ZonedDateTime observableEndTime;
  private ZonedDateTime observableStartTime;


}