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
  An audio facet is a grouping of characteristics unique to a digital representation of sound.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AudioFacet extends Facet {

  private String audioType;
  private Integer bitRate;
  private Integer duration;
  private String format;


}