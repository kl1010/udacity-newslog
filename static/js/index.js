// Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart1);
      google.charts.setOnLoadCallback(drawChart2);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart1() {

        // Create the data table.
        var data1 = new google.visualization.DataTable();
        data1.addColumn('string', 'Popular Article');
        data1.addColumn('number', 'views');
        data1.addRows([
          ['Candidate is Jerk', 338647],
          ['Bear Love Berries', 253801],
          ['Bad things Gone', 170098]
        ]);

        // Set chart options
        var options1 = {'title':'The most popluar three articles of all time'};

        // Instantiate and draw our chart, passing in some options.
        var chart1 = new google.visualization.PieChart(document.getElementById('chart_div1'));
        chart1.draw(data1, options1);
      }

      function drawChart2() {

        // Create the data table.
        var data2 = new google.visualization.DataTable();
        data2.addColumn('string', 'Popular Author');
        data2.addColumn('number', 'views');
        data2.addRows([
          ['Ursla La Multa', 507594],
          ['Rudolf von Treppenwitz', 423457],
          ['Anonymous Contributor', 170098],
          ['Markoff Chaney', 84557]
        ]);

        // Set chart options
        var options2 = {'title':'The most popluar Authors of All time'};

        // Instantiate and draw our chart, passing in some options.
        var chart2 = new google.visualization.PieChart(document.getElementById('chart_div2'));
        chart2.draw(data2, options2);
      }