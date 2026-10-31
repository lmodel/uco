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
  A relationship is a grouping of characteristics unique to an assertion that one or more objects are related to another object in some way.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Relationship extends UcoObject {

  private List<ZonedDateTime> endTime;
  private boolean isDirectional;
  private String kindOfRelationship;
  private List<UcoObject> source;
  private List<ZonedDateTime> startTime;
  private UcoObject target;


}