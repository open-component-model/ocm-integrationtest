package main

import (
	"bytes"
	"flag"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"reflect"
	"runtime"
	"strings"
	"testing"
	"text/template"
)

var binaryName = "ocm"

var binaryPath = "D:\\git\\ocm\\ocm\\cmds\\ocm\\"

var update = flag.Bool("update", false, "update golden case files")

func TestMain(m *testing.M) {
	err := os.Chdir(binaryPath)
	if err != nil {
		fmt.Printf("could not change dir: %v", err)
		os.Exit(1)
	}

	dir, err := os.Getwd()
	if err != nil {
		fmt.Printf("could not get current dir: %v", err)
	}

	binaryPath = filepath.Join(dir, binaryName)

	os.Exit(m.Run())
}

func runBinary(args []string) ([]byte, error) {
	cmd := exec.Command(binaryPath, args...)
	cmd.Env = append(os.Environ(), "GOCOVERDIR=.coverdata")
	return cmd.CombinedOutput()
}

func fixturePath(t *testing.T, fixture string) string {
	_, filename, _, ok := runtime.Caller(0)
	if !ok {
		t.Fatalf("problems recovering caller information")
	}
	return filepath.Join(filepath.Dir(filename), "cases", fixture)
}

func writeFixture(t *testing.T, fixture string, content []byte) {
	err := os.WriteFile(fixturePath(t, fixture), content, 0o644)
	if err != nil {
		t.Fatal(err)
	}
}

func loadFixture(t *testing.T, fixture string) string {
	tmpl, err := template.ParseFiles(fixturePath(t, fixture))
	if err != nil {
		t.Fatal(err)
	}
	var tmplBytes bytes.Buffer
	err = tmpl.Execute(&tmplBytes, envToMap())
	if err != nil {
		t.Fatal(err)
	}
	return tmplBytes.String()
}

func envToMap() map[string]string {
	evpMap := map[string]string{}

	for _, v := range os.Environ() {
		split := strings.Split(v, "=")
		if len(split) == 2 {
			evpMap[split[0]] = split[1]
		}
	}
	return evpMap
}

func TestCliArgs(t *testing.T) {
	tests := []struct {
		name    string
		args    []string
		fixture string
	}{
		{"no arguments", []string{}, "no-args.golden"},
		{"one argument", []string{"version"}, "one-argument.golden"},
		{"multiple arguments", []string{"--version"}, "multiple-arguments.golden"},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			output, err := runBinary(tt.args)

			if err != nil {
				t.Fatal(err)
			}

			if *update {
				writeFixture(t, tt.fixture, output)
			}

			actual := string(output)

			expected := loadFixture(t, tt.fixture)

			if !reflect.DeepEqual(actual, expected) {
				t.Fatalf("actual = %s, expected = %s", actual, expected)
			}
		})
	}
}
